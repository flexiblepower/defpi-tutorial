import logging
from .UniversalDimmer import UniversalDimmer
from defpi.ServiceMain import ServiceMain

from .InflexibleController.InflexibleControllerConnectionManagerImpl import InflexibleControllerConnectionManagerImpl

logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(name)20s %(levelname)8s - %(message)s',
                        datefmt='%H:%M:%S')

if __name__ == "__main__":
    ServiceMain().main(UniversalDimmer)
