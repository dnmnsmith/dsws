
.DEFAULT_GOAL := all

dsws:
	python -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. dsws.proto


all: dsws

clean:
	rm -f dsws_pb2.py
	rm -f dsws_pb2_grpc.py
	
install:
	@echo To install something...
	