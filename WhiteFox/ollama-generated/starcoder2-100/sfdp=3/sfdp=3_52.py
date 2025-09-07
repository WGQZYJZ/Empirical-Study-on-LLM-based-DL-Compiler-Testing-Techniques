
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1  = torch.matmul(x1, query.weight.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = softmax(v2)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)


# Initializing the model