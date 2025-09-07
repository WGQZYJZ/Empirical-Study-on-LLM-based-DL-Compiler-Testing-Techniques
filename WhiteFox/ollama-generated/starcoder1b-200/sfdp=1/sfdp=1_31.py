
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(32, 8, dtype=torch.float))
        self.key   = torch.nn.Parameter(torch.randn(16, 16, dtype=torch.float))
        self.value = torch.nn.Parameter(torch.randn(16, 16, dtype=torch.float))
        self.scale_factor = 0.25
 
        # The above model is not equivalent to the following one because both queries and keys need to have the same dimension:
        #     query = torch.zeros((32, 8), requires_grad=True)
        #     key   = torch.ones((16, 16))
        self.query  = nn.Parameter(torch.randn(32, 8, dtype=torch.float).view(-1))
        self.key    = nn.Parameter(torch.zeros(16, 16, dtype=torch.float).view(-1))
 
        # However, the following two model are equivalent:
        #     query = torch.randn((32, 8), requires_grad=True)
        #     key   = torch.ones((16, 16), requires_grad=True)
        self.query = nn.Parameter(torch.randn(32, 8, dtype=torch.float))
        self.key   = nn.Parameter(torch.ones(16, 16, dtype=torch.float))
 
    def forward(self):
        query = self.query
        key   = self.key
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / self.scale_factor
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = F.dropout(softmax_qk, p=0.25)
        output = dropout_qk.matmul(self.value)
        return output


# Initializing the model
m = Model()


