import './Form.css'
import 'bootstrap/dist/css/bootstrap.min.css';



const Form = () => {
    return (

        <section>
            <form>
            <label>
                Title: <input name="title" />
            </label>
            <hr />
            <label>
                Description: <input name="description" />
            </label>
            <hr />
            <label>
                Duration: <input name="duration" />
            </label>
            <hr />
            <label htmlFor="">
              Input: <input type="file" />
            </label>
            <hr />
            <input class="btn btn-primary" type="submit" value="Upload Video - Enviar"></input>
            </form>
        </section>
    )
}

export default Form