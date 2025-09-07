
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8013, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()
 
 
 # Inputs to the model 
 other = torch.randn(16, 1509).to(dtype=torch.float32)
x1 = torch.randn(8, 8013)
x2 = x1 + other

 # Initializing the model
m_initial  = Model()
 
 
 # Inputs to the model 
 __output__1 = m_initial(x1)
 
 m = Model().to(device)
 m(x2).shape
 
 torch.onnx.export(model=m,                   # model being run
                  args=(x2),                  # model inputs (or dict)
                  f='test_multiple_outputs_model.onnx',   # where to save the model
                  export_params=True,        # store the trained parameter weights inside the model file
                                          opset_version=10,             # the ONNX version to export the model to
                  do_constant_folding=False,  # whether to execute constant folding for optimization
                  input_names=['input'],   # the model's input names
                  output_names=['output1', 'output2'],        # the model's output names
                  dynamic_axes={'input' : {0: 'batch'},    # variable length axes
                                'output1': {0:'batch'}})

# Model 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3):
       print('forward')
       return output

 # Initializing the model 
 m = Model()
 
 
 # Inputs to the model
 input1  = torch.randn(450)
 input2  = torch.randn(450)
 input3  = torch.randn(450)

 