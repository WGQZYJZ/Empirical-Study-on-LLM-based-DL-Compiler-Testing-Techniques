
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x_input):
        v = torch.cat([x_input[:, :2], x_input[:, 3:]], dim=1)  # Concatenate the original input tensor and its second slice along dimension 1
        return v


# Initializing the model
m = Model()


