
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(128, 32 * 64)
 
    def forward(self, x1):
        q1 = self.qkv(x1).chunk(3, dim=1)
        query = q1[0].contiguous()
        key   = q1[1].contiguous()
        value = q1[2].contiguous()
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 64, 128, 128)
