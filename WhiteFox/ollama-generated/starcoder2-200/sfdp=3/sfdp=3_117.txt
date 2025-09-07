
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(3, 8)
 
    def forward(self, query, key, value):
        v1 = self.qk(query)
        v2 = v1 * scale_factor
        v3 = v2.softmax(-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = dropout_qk.matmul(value)

# Initializing the model
m  = Model()
 
# Inputs to the model
q = torch.randn(2048, 64)
k = torch.randn(2048, 3)
v = torch.randn(2048, 1)

 # Initializing parameters and hyperparameters
scale_factor = 5.960464477539062e-08
 
dropout_p=  0.1
 
 # Initializing the model output with the sample inputs above
m(q, k, v)

