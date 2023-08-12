package HomeWork.Dz3;

public class PasswordVerifier {
    /**
     * @param password Пароль
     */
    public void verifyPassword(String password) {
        if (password.length() < 8) {
            throw new IllegalArgumentException("Пароль должен быть не менее 8 символов");
        }

        boolean containsDigit = false;
        boolean containsUpperCase = false;

        for (char c : password.toCharArray()) {
            if (Character.isDigit(c)) {
                containsDigit = true;
            }

            if (Character.isUpperCase(c)) {
                containsUpperCase = true;
            }

            if (containsDigit && containsUpperCase) {
                return;
            }
        }

        throw new IllegalArgumentException("Пароль должен содержать хотя бы одну цифру и хотя бы одну заглавную букву");
    }
}
