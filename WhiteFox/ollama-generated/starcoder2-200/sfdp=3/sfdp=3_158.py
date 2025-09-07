
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):  # The model inputs are: two query tensors and a value tensor 
        v1 = torch.matmul(query, key.transpose(-2, -1))
        scale_factor = self.__computeScaleFactor()
        v2 = v1 * scale_factor
 
        v3 = v2.softmax(dim=-1)  # softmax() requires axis = -1
        dropout_p = self.__dropout()
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)
 
    def __computeScaleFactor(self):
        return (torch.norm(query, dim=-2).div_(torch.norm(key, dim=-1))).sqrt()  # sqrt() is not necessary here since scale factor should be positive
 
    def __dropout(self):
        return random.random() / self.__dropoutRatio(0)
 
 
def __dropoutRatio(n):
    