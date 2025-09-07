
class Model(torch.nn.Module):
    def __init__(self, channel=3, input_shape=(2048, 1, 1)):
        super().__init__()
        self.fc = torch.nn.Linear(input_shape[0], channel)
 
    def forward(self, x1):
        v1 = self.fc(x1).view(-1, self.fc.out_features)
        return v1


# Initializing the model
m = Model()

