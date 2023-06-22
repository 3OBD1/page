import logging
# print(dir(logging))
logging.basicConfig(filename="my_app.log", filemode="a",
                    format="%(asctime)s %(name)s %(levelname)s %(message)s  ")

# logging.critical("This Is critical Message")
# logging.error("This Is error Message")
the_logger = logging.getLogger("3obd")
the_logger.warning("This Is warning Message")
