# pytest -v -s -m "sanity" --capture=tee-sys --html=Reports/report.html testCases/
# pytest -v -s -m "regression" --capture=tee-sys --html=Reports/report.html testCases/
# pytest -v -s -m "sanity and regression" --capture=tee-sys --html=Reports/report.html testCases/
pytest -v -s -m "sanity or regression" --capture=tee-sys --html=Reports/report.html testCases/
