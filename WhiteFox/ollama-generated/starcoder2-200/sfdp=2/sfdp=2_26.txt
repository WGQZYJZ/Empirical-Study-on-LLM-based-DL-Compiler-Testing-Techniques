
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query, key, value):

        v1  = torch.matmul(query, key.transpose(-2,-1))

        v2  = self.v2()
        v3  = torch.ops._contrib_scale_factor(v1)

        v4  = torch.ops._scale_factor_softmax(torch.ops._dropout(v1, dropout_p))
        v5  = torch.ops._scale_factor_masked_softmax(v2, mask=None, scale_factor=0.)


        return v3


# Initializing the model
m  = Model()

# Input to the model: query, key and value

__query__, __key__, __value__ = [torch.randn(1, 8, 64, 2), torch.randn(1, 8, 64, 5), torch.randn(1, 3, 90, 7)]


