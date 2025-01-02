# Recipe_Hub
Django and Reactjs App

'''
      # Step 3: Run Tests
      - name: Run Tests
        working-directory: django
        run: docker compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"

      # Step 4: Run Linter (Flake8)
      - name: Run Linter
        working-directory: django
        run: docker compose run --rm app sh -c "flake8"
'''