
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(1024, 512)
 
    def forward(self, query, key, value):
        qk = self.qk(torch.cat([query, key], dim=-1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk @ value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(32, 1024, 768)
key = torch.randn(512, 2048, 768)
value = torch.randn(512, 2048, 768)
