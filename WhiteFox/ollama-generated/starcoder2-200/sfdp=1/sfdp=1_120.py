
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v4  = torch.nn.functional.dropout(softmax_qk, p=0.3)
        return output


# Initializing the model
m  = Model()


# Inputs to the model