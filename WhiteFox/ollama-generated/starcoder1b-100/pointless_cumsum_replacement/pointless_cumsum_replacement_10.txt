
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        return torch.full([input_tensor.shape[0], 1], 1, device=input_tensor.device) # Create a tensor filled with the scalar value 1 along dimension 0


# Initializing the model
m = Model()

