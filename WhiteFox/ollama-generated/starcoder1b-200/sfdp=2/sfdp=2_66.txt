
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v):
        super().__init__()
        self.W_q = torch.nn.Linear(d_k, d_k)  # Initialize linear weight matrix W_q (i.e. query layer), use pre-trained model weights to initialize
        self.W_k = torch.nn.Linear(d_v, d_k)  # Initialize linear weight matrix W_k (i.e. key layer), use pre-trained model weights to initialize
        self.W_o = torch.nn.Linear(d_k, d_v)  # Initialize linear weight matrix W_o (i.e. output layer), use pre-trained model weights to initialize
 
    def forward(self, x):
        x = torch.matmul(x, self.W_q.weight)
        x = torch.softmax(x, dim=-1)
        x = torch.matmul(x, self.W_k.weight)
        x = torch.matmul(x, self.W_o.weight)
        return x


# Initializing the model
m = Model(d_k=256, d_v=3072)


