
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Linear transformation on a flattened representation of the input tensor (of shape [batch_size * num_features] where batch_size is equal to the number of inputs and num_features is the number of channels in the image)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(4, 3, 64, 64)
