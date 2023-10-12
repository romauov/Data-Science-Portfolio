import catboost as cb
import pandas as pd

from flask import Flask, jsonify, request

# Load the model
model = cb.CatBoostClassifier()
model.load_model("cb_model.cbm")

# Init the app
app = Flask("default")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    in_X = request.get_json()
    feat_list = [' Destination Port', ' Flow Duration', ' Total Fwd Packets', ' Total Backward Packets',
                 'Total Length of Fwd Packets', ' Total Length of Bwd Packets', ' Fwd Packet Length Max',
                 ' Fwd Packet Length Min', ' Fwd Packet Length Mean', ' Fwd Packet Length Std', 'Bwd Packet Length Max',
                 ' Bwd Packet Length Min', ' Bwd Packet Length Mean', ' Bwd Packet Length Std', 'Flow Bytes/s',
                 ' Flow Packets/s', ' Flow IAT Mean', ' Flow IAT Std', ' Flow IAT Max', ' Flow IAT Min',
                 'Fwd IAT Total', ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max', ' Fwd IAT Min', 'Bwd IAT Total',
                 ' Bwd IAT Mean', ' Bwd IAT Std', ' Bwd IAT Max', ' Bwd IAT Min', 'Fwd PSH Flags', ' Fwd URG Flags',
                 ' Fwd Header Length', ' Bwd Header Length', 'Fwd Packets/s', ' Bwd Packets/s', ' Min Packet Length',
                 ' Max Packet Length', ' Packet Length Mean', ' Packet Length Std', ' Packet Length Variance',
                 'FIN Flag Count', ' SYN Flag Count', ' RST Flag Count', ' PSH Flag Count', ' ACK Flag Count',
                 ' URG Flag Count', ' CWE Flag Count', ' ECE Flag Count', ' Down/Up Ratio', ' Average Packet Size',
                 ' Avg Fwd Segment Size', ' Avg Bwd Segment Size', ' Fwd Header Length.1', 'Subflow Fwd Packets',
                 ' Subflow Fwd Bytes', ' Subflow Bwd Packets', ' Subflow Bwd Bytes', 'Init_Win_bytes_forward',
                 ' Init_Win_bytes_backward', ' act_data_pkt_fwd', ' min_seg_size_forward', 'Active Mean', ' Active Std',
                 ' Active Max', ' Active Min', 'Idle Mean', ' Idle Std', ' Idle Max', ' Idle Min']
    X = {cat:in_X[cat] for cat in feat_list}
    # Perform a prediction
    #preds = model.predict(pd.DataFrame(X, index=[0]))[0, 1]
    preds = model.predict(pd.DataFrame(X, index=[0]))[0][0]
    print(preds)
    # Output json with prediction
    result = {"prediction": preds}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)
