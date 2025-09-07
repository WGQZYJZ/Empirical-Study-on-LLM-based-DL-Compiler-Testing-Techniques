
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(23, 64)
        self.fc2 = torch.nn.Linear(64, 50)
 
    def forward(self, x):
        v1 = self.fc1(x)
        v2 = v1 * 2.37934482620906
        v3 = v1 * 1.65349392487631
        v4 = torch.sigmoid(v3)
        return v4
 
    def softmax_apply(self, x):
        self.softmax_layer = torch.nn.Softmax()
        result = self.softmax_layer(x)
        return result


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = torch.randn(100, 23) # Shape of [100, 23]
