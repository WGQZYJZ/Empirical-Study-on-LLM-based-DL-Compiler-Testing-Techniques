
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128 * 4 * 4, 30)
 
    def forward(self, x1):
        v1 = self.conv_bn_relu_pool1d_dropout_layernorm(x1) # Please refer to the document for more information about layer norm

        