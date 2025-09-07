
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, 0.5)
        # Add more layers after the dropout layer, such as t2 = t3 = t4 = ... = t_n = t_n+1 = ... = t_n+k
        return t2


# Initializing the model and running `replace_fx` optimization
config = torch.onnx.IValue(torch.randn(1, 2, 2))
torch.onnx.export(m, input=x1, f='model.onnx', export_params=False, opset_version=9)
gm = onnx_graph(f="model.onnx")
gm.replace_fx(config, True, 0.0, False, 2, 4)
gm.erase() # Remove the input tensor and set all output tensors to dynamic size, so as to avoid any potential out-of-memory errors
onnx.save(gm.model(), "model.onnx")


# Inputs to the model with onnxruntime python bindings or torch_script_demo
import onnxruntime as ort
sess = ort.InferenceSession("model.onnx")
x2 = sess.run([], {'x1': x1})[0]



