
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1  = torch.nn.functional.permute(y2)
        v3  = torch.nn.functional.bmm(x1, v1) # or torch.nn.functional.matmul(x1, v1) 
        return v3

# Initializing the model with 2 input tensors: x1 and y2<|end_of_tensor|>
m = Model()

