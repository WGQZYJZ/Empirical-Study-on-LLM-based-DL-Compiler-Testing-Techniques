    torch_out  = torch.tensor(eval(test_output), dtype=torch.__float__.type)

    assert torch._eq(torch_out, test_output).all()
