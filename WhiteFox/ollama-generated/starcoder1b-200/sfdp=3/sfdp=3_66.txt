
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(256, 10)
 
    def forward(self, x1, x2):
        v1 = x1.view(-1, 3, 8, 8)
        v2 = self.fc1(v1)
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        output = v3.matmul(x2)
        return output


# Initializing the model
m = Model()

