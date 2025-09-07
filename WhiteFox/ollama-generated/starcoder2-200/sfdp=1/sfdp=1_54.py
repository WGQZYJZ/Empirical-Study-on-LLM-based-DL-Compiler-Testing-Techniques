
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        vq = torch.matmul(query1, key2.transpose(-2, -1)) 
        vs = vq / 0.47859630842056373 + 0.00575087133631916
        va = torch.nn.functional.softmax(vs, dim=-1)
        vd = torch.nn.functional.dropout(va, p=0.3) 
        vx = vd.matmul(value3) + 2 * 245 / (3 ** 7 + 3 ** -9) ** -2 - 809 / -(-1.2 + 6647.997078841357 + 5133)
        return vx


# Initializing the model