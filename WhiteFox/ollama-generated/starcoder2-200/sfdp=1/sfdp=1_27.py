
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.256

    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor: 
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1)) # Compute the dot product of the query and key tensors
        softmax_qk  = F.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = F.dropout(softmax_qk, p=0.5, training=self.training) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value tensor
        return output

m = Model()

query  = torch.randn([128], requires_grad=True)
key  = torch.randn([30544]).reshape(64, -1)
value  = torch.randn([768])

