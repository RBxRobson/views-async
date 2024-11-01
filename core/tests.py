import pytest
from time import time
from .views import http_call_sync, http_call_async  # Altere 'your_module' para o nome correto

def test_http_call_sync(mocker):
    mock_print = mocker.patch("builtins.print")
    
    start_time = time()
    http_call_sync()
    end_time = time()
    
    # Ajuste a verificação do tempo
    assert 6 <= end_time - start_time <= 8
    
    # Verifique se a função print foi chamada corretamente
    mock_print.assert_any_call(0)
    mock_print.assert_any_call(5)
    mock_print.assert_any_call(f"Tempo total de execução (síncrono): {end_time - start_time:.2f} segundos")

@pytest.mark.asyncio
async def test_http_call_async(mocker):
    mock_print = mocker.patch("builtins.print")
    
    start_time = time()
    await http_call_async()
    end_time = time()
    
    # Ajuste a verificação do tempo
    assert 6 <= end_time - start_time <= 8
    
    # Verifique se a função print foi chamada corretamente
    mock_print.assert_any_call(0)
    mock_print.assert_any_call(5)
    mock_print.assert_any_call(f"Tempo total de execução (assíncrono): {end_time - start_time:.2f} segundos")
