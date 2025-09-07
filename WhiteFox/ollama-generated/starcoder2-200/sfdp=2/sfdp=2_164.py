
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.matmul(x1, x3)
        v4  = self.norm0(v2)
        v5 = self.attn0(x1, v7.transpose(-2,-1),  v8).softmax(dim=-1)
        v9 = torch.nn.functional.dropout(v5, p=self._args['attn_drop'])
        v6 = v3 * v4 + (torch.mean(v4 ** self.num_experts, -1)).unsqueeze(-1) 
        v10  = self.norm1(v7)
        v12  = torch.nn.functional.gelu(v9).matmul(self._args['head_gates'][None].expand([3*4,8]))
        v13 =  (self.drop0(torch.cat((v12, x6), dim=0)) ).transpose(-2,-1) 
        return torch.nn.functional.normalize(v9).matmul(x7).sum(dim=-2)


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(8,3*4*8,56 ,56 )
x3  = torch.randn(8,3*4*8, 170)
x4  = torch.randn(3 * 4 ,23)

