
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 384)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        softmax_v2  = (torch.nn.functional.softmax(v1, dim=-1)).mul(v1) # Apply softmax to the linear output
        dropout_v3 = torch.nn.functional.dropout(softmax_v2, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_v3
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 4096, 1024).mul(1e7)
