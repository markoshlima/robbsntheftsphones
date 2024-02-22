FROM jupyter/scipy-notebook

RUN pip install pandas scikit-learn scikit-learn xgboost flask flask_cors bz2file

COPY ./model.pbz2 ./model.pbz2
COPY ./base_to_single_predict.csv ./base_to_single_predict.csv
COPY bootstrap.sh ./bootstrap.sh
COPY main.py ./main.py

#RUN chmod +x ./bootstrap.sh

EXPOSE 8080

CMD ["./bootstrap.sh"]