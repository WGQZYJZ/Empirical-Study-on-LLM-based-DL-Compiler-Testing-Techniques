
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.fc = torch.nn.Linear(768, 1024)
 
    def forward(self, x):
        attention_output = self.fc(x.view(-1, 3*32*128))
        return attention_output


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(2, 512)
