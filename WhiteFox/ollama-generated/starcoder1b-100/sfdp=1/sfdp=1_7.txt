
class Model(torch.nn.Module):
    def __init__(self, dropout_p: float = 0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.dense = torch.nn.Linear(hidden_size, hidden_size)
 
    def forward(self, x):
        v = self.dense(x)  # Linear projection on the input and get an output tensor
        return v


# Initializing the model
m = Model()


