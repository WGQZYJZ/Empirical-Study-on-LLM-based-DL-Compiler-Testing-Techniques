
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4,8)
    
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -0.5)
        return torch.clamp_max(v2, 3.95709864)


# Initializing the model and printing the graph:
m  = Model()

torch.onnx.export(model=m,
                  args=(x1), # Arguments given to the model are not required for exporting to ONNX
                  input_names=["input"], 
                  output_names=["output"], 
                  verbose=True)

