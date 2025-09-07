
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.conv1d(x1, conv1.weight)  # the batch normalization layer is tracking running statistics.
        t3 = torch.nn.functional.batch_norm(t2, conv1.bias) 
        return t3

# Initializing the model
m  = Model()

