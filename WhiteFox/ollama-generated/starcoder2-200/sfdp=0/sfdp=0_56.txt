
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        scaled = torch.einsum("...ab,...bc->...ac", input1, input2) / invscale
        attention = scaled.softmax(dim=-1).matmul(input3)  # input3 is value tensor.
        return attention


# Initializing the model