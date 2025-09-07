
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Linear(3, 8) # query (B*N, C), key (B*M, C), value (B*N, H)
        self.key = torch.nn.Linear(3, 8) # qk1: (B*N, 2, 8), qk2: (B*M, 2, 8)
        self.value = torch.nn.Linear(3, 8) # value (B*N, H)
        self.softmax_qk1 = torch.nn.Softmax(-1) # softmax for query
        self.softmax_qk2 = torch.nn.Softmax(-1) # softmax for key
 
    def forward(self, x1):
        qk 1 = self.query(x1).transpose(0, 1).contiguous().view(x1.size(1), 8, -1)
        qk 2 = self.key(x1).view(x1.size(1), 8, -1)
        value = self.value(x1).view(x1.size(1), 8, -1)
        softmax_qk1 = self.softmax_qk1(qk1)
        output = softmax_qk1.matmul(value) # value is the last input to attention layer
 
        softmax_qk2 = self.softmax_qk2(qk2).transpose(0, 1).contiguous().view(x1.size(1), 8, -1)
        dropout_qk = softmax_qk2 + torch.randn(softmax_qk2.shape)
        output += dropout_qk # attention_output: (B*M, 2, 8)
 
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
