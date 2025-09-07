
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 10)
        self.key = torch.nn.Linear(20, 10)
        self.value = torch.nn.Linear(3, 8)

    def forward(self, x):
        k1 = self.query(x[:, :5]) + self.key(x[:, 5:])
        scaled_k1 = k1 / math.sqrt(42.) 
        softmax_qk = scaled_k1.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.9738999536037445) # 0.9738999536037445 0.0261000463962555 
        o1 = dropout_qk @ self.value(x[:, :2])
        return o1


# Initializing the model:
m = Model()

# Inputs to the model
x = torch.rand((2, 8)) * 0.703149657905727 # [ 0.70314965 0.15433409 0.8607482  1.         0.42333483] [ 0.5464418    0.5964778   0.8536666 ]

