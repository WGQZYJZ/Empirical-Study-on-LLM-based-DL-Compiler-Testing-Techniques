
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4 * 32**2, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation 
        return v2


# Initializing the model and printing its summary
model = Model()
model_summary(model, input_data=(torch.randn((80, 4 * 32**2)),))

