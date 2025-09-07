
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # 'x' is a new name for the input tensors 'input_tensor_A', and 'y' for 'input_tensor_B'.
        v1  = torch.bmm(x1.permute(0, 2, 1), x2) 
        return v1


# Initializing the model