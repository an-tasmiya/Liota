import logging
from liota.dccs.dcc import DataCenterComponent
from liota.entities.registered_entity import RegisteredEntity
from liota.entities.metrics.metric import Metric
from liota.entities.metrics.registered_metric import RegisteredMetric
from liota.entities.registered_entity import RegisteredEntity

log = logging.getLogger(__name__)

class CustomSocketDcc(DataCenterComponent):
    def __init__(self, comms):
        super(CustomSocketDcc, self).__init__(
            comms = comms
        )
    def register(self, entity_obj):
        if isinstance(entity_obj, Metric):
            return RegisteredMetric(entity_obj, self, None)
        else:
            return RegisteredEntity(entity_obj, self, None)

    def create_relationship(self, reg_entity_parent, reg_entity_child):
        reg_entity_child.parent = reg_entity_parent

    def _format_data(self, reg_metric):
        met_cnt = reg_metric.values.qsize()
        message = ''
        if met_cnt == 0:
            return
        for _ in range(met_cnt):
            v = reg_metric.values.get(block=True)
            print(v, type(v))
            if v is not None:
                # Graphite expects time in seconds, not milliseconds. Hence,
                # dividing by 1000
                message += '%s %s %d\n' % (reg_metric.ref_entity.name,
                                           v[1], v[0] / 1000)
        if message == '':
            return
        log.info ("Publishing values to Custom DCC")
        log.debug("Formatted message: {0}".format(message))
        return message

    def set_properties(self, reg_entity, properties):
        raise NotImplementedError

    def unregister(self, entity_obj):
        raise NotImplementedError
