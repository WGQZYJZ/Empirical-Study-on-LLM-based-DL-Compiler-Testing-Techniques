
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other  # other is an input to the model that you have to find (randomly or manually).
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1, other  = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 7, 7) # Note: you must provide 2 inputs that meet the criteria specified in the previous task

__output__  = m(x1).cpu().numpy()  # We are looking for the output of the model here! (Note this step can be automated by using ModelRunner)

