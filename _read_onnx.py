import onnx

onnx_model = onnx.load('./weights/yolov5s.onnx')

# Thêm thông tin về kích thước mẫu vào mô hình ONNX
onnx_model.graph.input[0].type.tensor_type.shape.dim[0].dim_value = 1

# Lưu mô hình ONNX đã có thông tin về kích thước mẫu vào tệp tin "yolov5s_batch1.onnx"
batch_onnx_path = 'yolov5s_batch1.onnx'
onnx.save(onnx_model, batch_onnx_path)