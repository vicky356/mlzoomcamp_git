FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

RUN pip install pillow

COPY hw_function.py .
ENV MODEL_NAME=bees-wasps-v2.tflite

CMD ["hw_function.lambda_handler"]