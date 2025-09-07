
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale = torch.Tensor([0.5, 1., 2., 4., 8.]) 
        self.dropout = nn.Dropout()
        self.linear = nn.Linear(32, 6)
 
    def forward(self, query):
        v_query = self.dropout(query.clone())
 
        k = torch.nn.Parameter(torch.rand(10, 4))
        v = torch.nn.Parameter(torch.rand(10, 8))
        qk = torch.matmul(v_query, k) * 1e-5 # Scale the dot product by 1e-5
        scaled_qk = qk / self.scale[7] 
        
        softmax_qk = scaled_qk.softmax(-1) 
        dropout_qk = self.dropout(softmax_qk)
        output = torch.einsum('ij, ij -> i', v, dropout_qk)
        return output
