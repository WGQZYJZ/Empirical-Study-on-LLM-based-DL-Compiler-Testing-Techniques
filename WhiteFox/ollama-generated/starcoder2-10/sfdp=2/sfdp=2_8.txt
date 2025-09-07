
class Model(torch.nn.Module):
    def __init__(self, scale = 0.125):
        super().__init__()
        self.scale = torch.tensor([scale])
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk / self.scale[0]
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self.p) 
        output  = dropout_qk @ value
        return output


# Initializing the model
m  = Model()
# Inputs to the model (the query should not be necessary since we are only evaluating the dot product of a query and key; however this is added for completeness):
query, key, value  = torch.randn(128,32), torch.randn(128, 640, 32), torch.randn(579)
__output__   = m(query, key, value).shape  # __output__  is the output of the model (a tensor of size 579)

