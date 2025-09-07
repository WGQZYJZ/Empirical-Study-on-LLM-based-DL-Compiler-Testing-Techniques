
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x_tensor):
        v = torch.cat([x_tensor[:, 0:9223372036854775807], x_tensor[:, 9223372036854775807:]], dim=1) # Sliced the input tensor along dimension 1
        return v

# Initializing the model
m = Model()

