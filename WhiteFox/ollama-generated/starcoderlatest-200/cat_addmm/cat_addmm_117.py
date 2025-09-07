
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.addmm = torch.nn.AddMM(reduction="sum")
 
    def forward(self, x1):
        t1 = self.addmm(x1, mat1, mat2)
        t2 = torch.cat([t1], dim)
        return t2

# Initializing the model
m = Model()


class AddMMTest(nn.Module):
    def __init__(self):
        super().__init__()

    def test_addmm_output(self, addmm_test):
        x = torch.rand([1, 3, 224, 224])

        # generate and check the output of the AddMM function
        addmm_out = addmm_test(x)
        self.assertTensorsEqual(addmm_out, expected_output, prec=0)

    def assertTensorsEqual(self, out1, out2, prec):
        assert TensorsEqual(out1, out2, prec), \
            "Error: tensors not close enough"

    @staticmethod
    def generate_tensor():
        