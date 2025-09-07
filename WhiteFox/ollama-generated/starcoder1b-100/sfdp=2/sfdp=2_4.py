
class Model(torch.nn.Module):
    def __init__(self, dim_model=8, dropout=0.1):
        super().__init__()
        self.dim_model = dim_model
        self.fc = torch.nn.Linear(2 * dim_model, dim_model)
        self.dropout = nn.Dropout(p=dropout)
 
    def forward(self, x):
        h = torch.relu(torch.matmul(x.view(-1, 2 * self.dim_model),
                                   self.fc.weight.transpose(0, 1)))
        return self.dropout(h)


# Initializing the model
m = Model()


