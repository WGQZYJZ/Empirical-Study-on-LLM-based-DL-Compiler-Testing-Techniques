
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1, 
                                         self.linear.weight[:, None, :], 
                                         self.linear.bias) 
        return torch.argmax(v1.permute(-2), axis=0)


# Initializing the model
m = Model()


