
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensor):
        v1 = torch.cat([input_tensor, input_tensor], dim=1)
        v2 = v1[:, 0:size]
        return v2


# Initializing the model
m = Model()


