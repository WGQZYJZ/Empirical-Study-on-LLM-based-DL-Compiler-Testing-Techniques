
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 64)
 
    def forward(self, x, key, value, query, dropout_p=0.1):
        attn = self.attn(x).unsqueeze(dim=-2).unsqueeze(dim=-3) # Add the input as an additional axis in front of dimensions -2 and -3
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / (self.scale ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return attn, qk, scaled_qk, softmax_qk, dropout_qk, output


# Initializing the model
m = Model()


